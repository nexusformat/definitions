(add-hook
  'nxml-mode-hook
  (lambda ()
    (setq rng-schema-locating-files-default
          (append '("/home/prjemian/Documents/eclipse/NeXus/definitions/trunk/xslt/docbook-xsl-1.75.2/locatingrules.xml")
                  rng-schema-locating-files-default ))))
