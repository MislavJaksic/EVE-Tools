# import datetime
# from eve_tools.file_cacher import JsonFileCacher
#
#
# market_history_stalness_days = 3
# market_order_stalness_hours = 24
#
#
# class APIGetter(object):
#     def __init__(self):
#         self.file_cacher = JsonFileCacher()
#
#     def get_corp_npccorps_ids(self, stale_after=None):
#         filename = "corporation_npccorps_ids.json"
#         uri = "https://esi.evetech.net/latest/corporations/npccorps/?datasource=tranquility"
#
#         return self.file_cacher.get_uri_to_file_if_stale(uri, filename, stale_after)
#
#     def get_corp_info(self, id, stale_after=None):
#         filename = "corporation_info_{}.json".format(str(id))
#         uri = "https://esi.evetech.net/latest/corporations/{}/?datasource=tranquility".format(
#             str(id)
#         )
#
#         return self.file_cacher.get_uri_to_file_if_stale(uri, filename, stale_after)
#
#     def get_corp_store_offers(self, id, stale_after=None):
#         filename = "corporation_store_{}.json".format(str(id))
#         uri = "https://esi.evetech.net/latest/loyalty/stores/{}/offers/?datasource=tranquility".format(
#             str(id)
#         )
#
#         return self.file_cacher.get_uri_to_file_if_stale(uri, filename, stale_after)
#
#     def get_market_region_item_history(
#         self,
#         region_id,
#         item_id,
#         stale_after=datetime.timedelta(days=market_history_stalness_days),
#     ):
#         filename = "market_history_region_{}_item_{}.json".format(
#             str(region_id), str(item_id)
#         )
#         uri = "https://esi.evetech.net/latest/markets/{}/history/?datasource=tranquility&type_id={}".format(
#             str(region_id), str(item_id)
#         )
#
#         return self.file_cacher.get_uri_to_file_if_stale(uri, filename, stale_after)
#
#     def get_market_region_item_order_type_page(
#         self,
#         region_id,
#         item_id,
#         order_type,
#         page,
#         stale_after=datetime.timedelta(hours=market_order_stalness_hours),
#     ):
#         filename = "market_order_{}_region_{}_item_{}_page_{}.json".format(
#             order_type, str(region_id), str(item_id), str(page)
#         )
#         uri = "https://esi.evetech.net/latest/markets/{}/orders/?datasource=tranquility&order_type={}&page={}&type_id={}".format(
#             str(region_id), order_type, str(page), str(item_id)
#         )
#
#         return self.file_cacher.get_uri_to_file_if_stale(uri, filename, stale_after)
#
#     def get_market_group_ids(self, stale_after=None):
#         filename = "market_group_ids.json"
#         uri = "https://esi.evetech.net/latest/markets/groups/?datasource=tranquility"
#
#         return self.file_cacher.get_uri_to_file_if_stale(uri, filename, stale_after)
#
#     def get_market_group_info(self, id, stale_after=None):
#         filename = "market_group_info_{}.json".format(id)
#         uri = "https://esi.evetech.net/latest/markets/groups/{}/?datasource=tranquility&language=en-us".format(
#             id
#         )
#
#         return self.file_cacher.get_uri_to_file_if_stale(uri, filename, stale_after)
#
#     def get_universe_region_ids(self, stale_after=None):
#         filename = "region_ids.json"
#         uri = "https://esi.evetech.net/latest/universe/regions/?datasource=tranquility"
#
#         return self.file_cacher.get_uri_to_file_if_stale(uri, filename, stale_after)
#
#     def get_universe_region_info(self, id, stale_after=None):
#         filename = "region_info_{}.json".format(str(id))
#         uri = "https://esi.evetech.net/latest/universe/regions/{}/?datasource=tranquility".format(
#             str(id)
#         )
#
#         return self.file_cacher.get_uri_to_file_if_stale(uri, filename, stale_after)
#
#     def get_universe_type_page(self, page, stale_after=None):
#         filename = "type_page_{}.json".format(str(page))
#         uri = "https://esi.evetech.net/latest/universe/types/?datasource=tranquility&page={}".format(
#             str(page)
#         )
#
#         return self.file_cacher.get_uri_to_file_if_stale(uri, filename, stale_after)
#
#     def get_universe_type_info(self, id, stale_after=None):
#         filename = "type_info_{}.json".format(str(id))
#         uri = "https://esi.evetech.net/latest/universe/types/{}/?datasource=tranquility".format(
#             str(id)
#         )
#
#         return self.file_cacher.get_uri_to_file_if_stale(uri, filename, stale_after)
