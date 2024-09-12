import scrapy
from scrapy.http import HtmlResponse

from pep_parse.constants import PROTOCOL, TARGET_DOMAINS
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = TARGET_DOMAINS
    start_urls = [f"{PROTOCOL}://{domain}/" for domain in TARGET_DOMAINS]

    def parse(self, response: HtmlResponse):
        pep_rows = response.css("#numerical-index tbody>tr")
        for row in pep_rows:
            number, name = row.css("a::text").getall()
            yield response.follow(
                row.css("a::attr(href)").get(),
                callback=self.parse_pep,
                cb_kwargs={
                    "number": number,
                    "name": name,
                },
            )

    def parse_pep(self, response: HtmlResponse, number: str, name: str):
        status: str = response.css(
            "#pep-content dt:contains('Status')+dd>abbr::text"
        ).get()
        data = {
            "number": int(number),
            "name": name.strip(),
            "status": status.strip(),
        }
        yield PepParseItem(data)
