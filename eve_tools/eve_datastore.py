from eve_tools.swagger_client.api.universe_api import UniverseApi


class EveDatastore:
    def __init__(self):
        self.universe_api = UniverseApi()

    def get_universe_system_kills(self):
        systems = self.universe_api.get_universe_systems()

        empty_kills = []
        for system in systems:
            empty = {"npc_kills": 0, "pod_kills": 0, "ship_kills": 0}
            empty["system_id"] = system
            empty_kills.append(empty)

        system_kills = self.universe_api.get_universe_system_kills()
        for system_kill in system_kills:
            for empty_kill in empty_kills:
                if empty_kill["system_id"] == system_kill["system_id"]:
                    empty_kill["npc_kills"] = system_kill["npc_kills"]
                    empty_kill["pod_kills"] = system_kill["pod_kills"]
                    empty_kill["ship_kills"] = system_kill["ship_kills"]

        return empty_kills
