from collections import Callable

from triangulum.controllers.base import BaseController


class Kingdom(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='kingdom')

    async def cancel_governor(self, governor_player_id: int) -> dict:
        """Removes a governor from the kingdom

        Args:
            governor_player_id: ID of the governor player

        Returns:
            dict
        """
        return await self.invoke_action(
            action='cancelGovernor',
            params={
                'governorPlayerId': governor_player_id,
            }
        )

    async def accept_invitation(self, id: int) -> dict:
        """Accept an invitation to a kingdom
        (to either become a governor, a duke or to relocate) *

        Args:
            id: ID of the invitation

        Returns:
            dict
        """
        return await self.invoke_action(
            action='acceptInvitation',
            params={
                'id': id,
            }
        )

    async def get_top3_nearby_kings(self, village_id: int) -> dict:
        """Get top 3 kings nearest to village_id

        Args:
            village_id: ID of the village

        Returns:
            dict
        """
        return await self.invoke_action(
            action='getTop3NearbyKings',
            params={
                'villageId': village_id,
            }
        )

    async def start_coronation_ceremony(self, village_id: int, tag: str) -> dict:
        """UNKNOWN *

        Args:
            village_id: ID of the village
            tag: UNKNOWN *

        Returns:
            dict
        """
        return await self.invoke_action(
            action='startCoronationCeremony',
            params={
                'villageId': village_id,
                'tag': tag,
            }
        )

    async def change_tag(self, tag: str) -> dict:
        """UNKNOWN *

        Args:
            tag: UNKNOWN *

        Returns:
            dict
        """
        return await self.invoke_action(
            action='changeTag',
            params={
                'tag': tag,  # TODO: wtf is this
            }
        )

    async def promote_to_duke(self, player_id: int, custom_text: str) -> dict:
        """Invite a player to become a duke

        Args:
            player_id: ID of the player to invite
            custom_text: Message to include in the invitation

        Returns:
            dict
        """
        return await self.invoke_action(
            action='promoteToDuke',
            params={
                'playerId': player_id,
                'customText': custom_text,
            }
        )

    async def change_description(self, group_id: int, public_description: str) -> dict:
        """Change the publicly visible description of your kingdom

        Args:
            group_id: ID of the kingdom
            public_description: Description to set

        Returns:
            dict
        """
        return await self.invoke_action(
            action='changeDescription',
            params={
                'groupId': group_id,
                'publicDescription': public_description,
            }
        )

    async def decline_invitation(self, id: int) -> dict:
        """Decline an invitation to a kingdom

        Args:
            id: ID of the invitation

        Returns:
            dict
        """
        return await self.invoke_action(
            action='declineInvitation',
            params={
                'id': id,
            }
        )

    async def get_fight_strength_ranks(self) -> dict:
        """Get Fight Strength rankings of your kingdom *

        Returns:
            dict
        """
        return await self.invoke_action(
            action='getFightStrengthRanks'
        )

    async def get_news(self, start: int, count: int) -> dict:
        """UNKNOWN

        Args:
            start: Index to start fetching from
            count: Index to stop fetching at

        Returns:
            dict
        """
        return await self.invoke_action(
            action='getNews',
            params={
                'start': start,
                'count': count,
            }
        )

    async def change_internal_description(self, group_id: int, internal_description: str) -> dict:
        """Change the internally visible description of your kingdom

        Args:
            group_id: ID of the kingdom
            internal_description: Description to be set

        Returns:
            dict
        """
        return await self.invoke_action(
            action='changeInternalDescription',
            params={
                'groupId': group_id,
                'internalDescription': internal_description,
            }
        )

    async def get_duke_candidate(self, kingdom_id: int) -> dict:
        """Get governors best suited to become Dukes in your kingdom

        Args:
            kingdom_id: ID of the kingdom

        Returns:
            dict
        """
        return await self.invoke_action(
            action='getDukeCandidate',
            params={
                'kingdomId': kingdom_id,
            }
        )

    async def cancel_kingdom(self) -> dict:
        """Disband a kingdom

        Returns:
            dict
        """
        return await self.invoke_action(
            action='cancelKingdom'
        )
