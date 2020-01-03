from typing import Union, List, Callable

from cachetools import TTLCache

from triangulum.controllers.base import BaseController
from triangulum.utils.cache import cached, MAX_SIZE, TTL
from triangulum.utils.enums import BrightSocietyTarget, DarkSocietyTarget, BrightSocietyAdmissionCondition, \
    DarkSocietyAdmissionCondition, SocietySharedInformation, SocietyAttitude


class Society(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='society')

    @cached(TTLCache(MAX_SIZE, TTL))
    async def get_shared_informations(self, village_id: int) -> dict:
        """UNKNOWN *

        Args:
            village_id: ID of a village

        Returns:
            dict
        """
        return await self.invoke_action(
            action='getSharedInformations',
            params={
                'villageId': village_id,
            }
        )

    async def create(
        self,
        name: str,
        attitude: SocietyAttitude,
        target: Union[BrightSocietyTarget, DarkSocietyTarget],
        target_id: int,
        join_condition: Union[BrightSocietyAdmissionCondition, DarkSocietyAdmissionCondition],
        condition_value: int,
        share_battle_and_scout_reports: bool,
        share_display_of_next_attack_on_village: bool,
        share_additional_village_information: bool
    ) -> dict:
        """Create a secret society
        The target and join_condition depend on the attitude of the society

        Args:
            name: Name of the secret society
            attitude: Attitude of the secret society
            target: Target type of the secret society
            target_id: ID of the target entity
            join_condition: Condition type for joining
            condition_value: Value for join_condition
            share_battle_and_scout_reports: Toggle for whether the society shares battle and scout reports
            share_display_of_next_attack_on_village: Toggle for whether the society displays the incoming attacks
                on eachothers villages
            share_additional_village_information: Toggle for whether additional information is shared between
                the members of the society, such as crop production and troop counts

        Returns:
            dict
        """
        params = {
                'name': name,
                'attitude': attitude.value,
                'target': target.value,
                'targetId': target_id,
                'sharedInformations': {
                    SocietySharedInformation.BATTLE_AND_SCOUT_REPORTS.value: share_battle_and_scout_reports,
                    SocietySharedInformation.DISPLAY_OF_NEXT_ATTACK_ON_VILLAGE.value: share_display_of_next_attack_on_village,
                    SocietySharedInformation.ADDITIONAL_VILLAGE_INFORMATION.value: share_additional_village_information
                }
            }
        if not target == BrightSocietyTarget.PROTECT_EACH_OTHER:
            params['joinCondition'] = join_condition.value
            params['conditionValue'] = condition_value

        return await self.invoke_action(
            action='create',
            params=params
        )

    async def invite(self, group_id: int, player_names: List[str], custom_text: str) -> dict:
        """Invite players to a secret society

        Args:
            group_id: ID of the secret society
            player_names: List of player names to be invited
            custom_text: Message to include with the invitation

        Returns:
            dict
        """
        return await self.invoke_action(
            action='invite',
            params={
                'groupId': group_id,
                'groupType': 2,  # Doesn't seem like there's any others right now
                'playerName': player_names,
                'customText': custom_text,
            }
        )

    async def decline_invitation(self, id: int) -> dict:
        """Decline a secret society invitation

        Args:
            id: ID of the invitation

        Returns:

        """
        return await self.invoke_action(
            action='declineInvitation',
            params={
                'id': id,
            }
        )

    async def change_description(self, group_id: int, description: int) -> dict:
        """Change a secret society description

        Args:
            group_id: ID of the secret society
            description: New description

        Returns:

        """
        return await self.invoke_action(
            action='changeDescription',
            params={
                'groupId': group_id,
                'description': description,
            }
        )

    async def close(self, group_id: int) -> dict:
        """Close a secret society

        Args:
            group_id: ID of the secret society

        Returns:
            dict
        """
        return await self.invoke_action(
            action='close',
            params={
                'groupId': group_id,
                'groupType': 2,  # Doesn't seem like there's any others right now
            }
        )
