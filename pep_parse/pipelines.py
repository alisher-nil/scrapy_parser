import csv
from collections import Counter
from datetime import datetime

from pep_parse.constants import BASE_DIR, OUTPUT_DIR
from pep_parse.items import PepParseItem


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_counter = Counter()

    def process_item(self, item: PepParseItem, spider):
        self.status_counter[item["status"]] += 1
        return item

    def close_spider(self, spider):
        result = [("Статус", "Количество")]
        result.extend(self.status_counter.most_common())
        result.append(["Total", sum(self.status_counter.values())])

        now_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = BASE_DIR / OUTPUT_DIR / f"status_summary_{now_str}.csv"
        with open(filename, "w", newline="", encoding="utf-8") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerows(result)
