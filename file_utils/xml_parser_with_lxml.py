from lxml import etree

parser = etree.XMLParser(ns_clean=True, recover=True)

NAMESPACE = {
    'nvd': 'http://nvd.nist.gov/feeds/nvdcvestatements'
}

vs_file = '/Users/nixdaemon/Downloads/vendorstatements.xml'

xml = etree.parse(vs_file, parser)

root = xml.getroot()

published_date = root.attrib['publish_date']

for entry in root:
    organization = entry.attrib['organization']
    last_modified = entry.attrib['lastmodified']
    cve_id = entry.attrib['cvename']
    contributor = entry.attrib['contributor']
    summary = entry.text
    print(entry.attrib['lastmodified'])


