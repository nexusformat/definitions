import datetime
import json
import os
from pathlib import Path
from typing import Optional

import lxml
import yaml

from ..globals import directories
from ..globals.nxdl import get_nxdl_version
from ..globals.urls import MANUAL_URL
from ..utils.types import PathLike


class AnchorRegistry:
    """Document the NXDL vocabulary. Usage goes as follows

    .. code:: python

        reg = AnchorRegistry(output_path=...)
        # It loaded the existing registry from file (if provided)

        reg.add(...)
        reg.add(...)
        ...
        anchors = reg.flush_anchor_buffer()

        reg.add(...)
        reg.add(...)
        ...
        anchors = reg.flush_anchor_buffer()

        ...
        reg.write()
        # It saved the in-memory registry to file (if provided)
    """

    def __init__(self, output_path: Optional[PathLike] = None) -> None:
        # For example: output_path = get_build_root() / "manual" / "source" / "_static"
        self._writing_enabled = bool(output_path)
        if output_path:
            base = "nxdl_vocabulary"
            output_path = Path(output_path).absolute()
            output_path.mkdir(parents=True, exist_ok=True)
            self._html_file = output_path / f"{base}.html"
            self._txt_file = output_path / f"{base}.txt"
            self._json_file = output_path / f"{base}.json"
            self._yaml_file = output_path / f"{base}.yml"
        else:
            self._html_file = None
            self._txt_file = None
            self._json_file = None
            self._yaml_file = None
        self._registry = self._load_registry()
        self._anchor_buffer = []
        self._nxdl_file = None

    @property
    def all_anchors(self):
        result = []
        for v in self._registry.values():
            result += list(v.keys())
        return result

    @property
    def nxdl_file(self) -> Optional[Path]:
        return self._nxdl_file

    @nxdl_file.setter
    def nxdl_file(self, value: PathLike) -> None:
        self._nxdl_file = Path(value).absolute()

    @property
    def html_url(self):
        rst_file = directories.get_rst_filename(self.nxdl_file)
        manual_root = directories.manual_build_sphinxroot()
        rel_path = rst_file.relative_to(manual_root)
        rel_html = str(rel_path.with_suffix(".html"))
        rel_html = rel_html.replace(os.sep, "/")
        return f"{MANUAL_URL}/{rel_html}"

    def add(self, anchor):
        """Add anchor to the in-memory registry and to the
        current anchor buffer."""
        if anchor not in self._anchor_buffer:
            self._anchor_buffer.append(anchor)

        key = self._key_from_anchor(anchor)

        if key not in self._registry:
            self._registry[key] = {}

        reg = self._registry[key]
        if anchor not in reg:
            hanchor = self._html_anchor(anchor)
            url = f"{self.html_url}{hanchor}"
            reg[anchor] = dict(
                term=anchor,
                html=hanchor,
                url=url,
            )

    def _key_from_anchor(self, anchor):
        key = anchor.lower().split("/")[-1].split("@")[-1].split("-")[0]
        if "@" in anchor:
            # restore preceding "@" symbol
            key = "@" + key
        return key

    def write(self):
        """Write the in-memory registry to files"""
        if not self._writing_enabled:
            return
        contents = dict(
            _metadata=dict(
                datetime=datetime.datetime.utcnow().isoformat(),
                title="NeXus NXDL vocabulary.",
                subtitle="Anchors for all NeXus fields, groups, "
                "attributes, and links.",
                version=get_nxdl_version(),
            ),
            terms=self._registry,
        )
        self._write_yaml(contents)
        self._write_json(contents)
        self._write_txt()
        self._write_html(contents)

    def flush_anchor_buffer(self) -> list:
        """Flush the anchor buffer"""
        self._anchor_buffer, ret = list(), self._anchor_buffer
        return ret

    def _html_anchor(self, anchor):
        """
        Create (internal hyperlink target for) HTML anchor from reST anchor.

        Example:

        * reST anchor: /NXcanSAS/ENTRY/TRANSMISSION_SPECTRUM@timestamp-attribute
        * HTML anchor: #nxcansas-entry-transmission-spectrum-timestamp-attribute
        """
        html_anchor = (
            anchor.lower()
            .lstrip("/")
            .replace("_", "-")
            .replace("@", "-")
            .replace("/", "-")
        )
        return f"#{html_anchor}"

    def _load_registry(self) -> dict:
        """Load the anchor registry in memory."""
        if not self._yaml_file:
            return {}
        registry = None
        if self._yaml_file.exists():
            contents = yaml.load(open(self._yaml_file, "r").read(), Loader=yaml.Loader)
            if contents is not None:
                registry = contents.get("terms")
        return registry or {}

    def _write_html(self, contents):
        """Write the anchors to an HTML file."""
        if not self._html_file:
            return
        root = lxml.etree.Element("html")
        body = lxml.etree.SubElement(root, "body")
        title = lxml.etree.SubElement(body, "h1")
        subtitle = lxml.etree.SubElement(body, "em")

        title.text = contents["_metadata"]["title"].strip(".")
        subtitle.text = contents["_metadata"]["subtitle"].strip(".")
        vocab_list = lxml.etree.SubElement(body, "h2")
        vocab_list.text = "NXDL Vocabulary"

        p = lxml.etree.SubElement(body, "p")
        p.text = "This content is also available in these formats: "
        for ext in "json txt yml".split():
            a = lxml.etree.SubElement(p, "a")
            a.attrib["href"] = f"{MANUAL_URL}/_static/{self._txt_file.stem}.{ext}"
            a.text = f" {ext}"

        dl = lxml.etree.SubElement(body, "dl")
        for term, termlist in sorted(contents["terms"].items()):
            dterm = lxml.etree.SubElement(dl, "dt")
            dterm.text = term
            for _, itemdict in sorted(termlist.items()):
                ddef = lxml.etree.SubElement(dterm, "dd")
                a = lxml.etree.SubElement(ddef, "a")
                a.attrib["href"] = itemdict["url"]
                a.text = itemdict["term"]

        lxml.etree.SubElement(body, "hr")

        foot = lxml.etree.SubElement(body, "p")
        foot_em = lxml.etree.SubElement(foot, "em")
        foot_em.text = f"written: {contents['_metadata']['datetime']}"

        html = lxml.etree.tostring(root, pretty_print=True).decode()
        with open(self._html_file, "w") as f:
            f.write(html)
            f.write("\n")

    def _write_json(self, contents):
        if not self._json_file:
            return
        with open(self._json_file, "w") as f:
            json.dump(contents, f, indent=4, sort_keys=True)
            f.write("\n")

    def _write_txt(self):
        """Compendium (dump the list of all known anchors in raw form)."""
        if not self._txt_file:
            return
        terms = self.all_anchors
        with open(self._txt_file, "w") as f:
            f.write("\n".join(sorted(terms)))
            f.write("\n")

    def _write_yaml(self, contents):
        if not self._yaml_file:
            return
        with open(self._yaml_file, "w") as f:
            yaml.dump(contents, f)
