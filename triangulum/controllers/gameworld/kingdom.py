from collections import Callable

from triangulum.controllers.base import BaseController


class Kingdom(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='kingdom')

    async def cancel_governor(self, governor_player_id: int) -> dict:
        return await self.invoke_action(
            action='cancelGovernor',
            params={
                'governorPlayerId': governor_player_id,
            }
        )

    async def accept_invitation(self, id: int) -> dict:
        return await self.invoke_action(
            action='acceptInvitation',
            params={
                'id': id,
            }
        )

    async def get_top3_nearby_kings(self, village_id: int) -> dict:
        return await self.invoke_action(
            action='getTop3NearbyKings',
            params={
                'villageId': village_id,
            }
        )

    async def start_coronation_ceremony(self, village_id: int, tag: str) -> dict:
        return await self.invoke_action(
            action='startCoronationCeremony',
            params={
                'villageId': village_id,
                'tag': tag,  # TODO: wtf is this
            }
        )

    async def change_tag(self, tag: str) -> dict:
        return await self.invoke_action(
            action='changeTag',
            params={
                'tag': tag,  # TODO: wtf is this
            }
        )

    async def promote_to_duke(self, player_id: int, custom_text: str) -> dict:
        return await self.invoke_action(
            action='promoteToDuke',
            params={
                'playerId': player_id,
                'customText': custom_text,
            }
        )

    async def change_description(self, group_id: int, public_description: str) -> dict:
        return await self.invoke_action(
            action='changeDescription',
            params={
                'groupId': group_id,
                'publicDescription': public_description,
            }
        )

    async def decline_invitation(self, id: int) -> dict:
        return await self.invoke_action(
            action='declineInvitation',
            params={
                'id': id,
            }
        )

    async def get_fight_strength_ranks(self) -> dict:
        return await self.invoke_action(
            action='getFightStrengthRanks'
        )

    async def get_news(self, start: int, count: int) -> dict:
        return await self.invoke_action(
            action='getNews',
            params={
                'start': start,
                'count': count,
            }
        )

    async def change_internal_description(self, group_id: int, internal_description: str) -> dict:
        return await self.invoke_action(
            action='changeInternalDescription',
            params={
                'groupId': group_id,
                'internalDescription': internal_description,
            }
        )

    async def get_duke_candidate(self, kingdom_id: int) -> dict:
        return await self.invoke_action(
            action='getDukeCandidate',
            params={
                'kingdomId': kingdom_id,
            }
        )

    async def cancel_kingdom(self) -> dict:
        return await self.invoke_action(
            action='cancelKingdom'
        )
