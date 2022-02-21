from scrapy.exporters import CsvItemExporter

FIELDNAMES = ['name', 'images', 'price', 'url', 'description']


class KproektPipeline:
    def __init__(self):
        self.file = open('product_data.csv', 'wb')
        self.exporter = CsvItemExporter(self.file, encoding='utf-8',
                                        fields_to_export=FIELDNAMES)
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item