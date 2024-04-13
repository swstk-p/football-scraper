from .base import BaseSpider, scrapy
from pprint import pp


class ClubNameSpider(BaseSpider):
    name = "club_name"

    def __init__(self):
        super().__init__()

    def start_requests(self):
        """Checks if teams for all the leagues in all seasons are available; if not then generates url for each league each season and sends request

        Yields:
            _type_: scrapy.Request
        """
        # have_all_club_names = self.club_names.have_all_leagues_seasons_club_names()
        # if not have_all_club_names:
        #     all_clubs_urls_info = self.club_names.get_all_seasons_leagues_url()
        #     for url_info in all_clubs_urls_info:
        #         yield scrapy.Request(
        #             url=url_info["url"],
        #             callback=self.club_names.all_club_names_callback,
        #             cb_kwargs={
        #                 "league": url_info["league"],
        #                 "season": url_info["season"],
        #             },
        #         )

        all_clubs_urls_info = self.club_names.get_all_seasons_leagues_url()
        for url_info in all_clubs_urls_info:
            yield scrapy.Request(
                url=url_info["url"],
                callback=self.parse,
                cb_kwargs={
                    "league": url_info["league"],
                    "season": url_info["season"],
                },
            )

    def parse(self, response, league, season):
        """Parses the club names from the response and writes them

        Args:
            response (_type_): response object from spider
            league (_type_): league name
            season (_type_): season
        """
        clubs = self.club_names.parse_club_names(response, league, season)
        # self.club_names.write_to_json_file(clubs)
        # print("***********************************************************")
        # pp(f"club_name: {clubs}", width=1)
        # print("***********************************************************")
