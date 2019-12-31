from typing import Union, List, Callable

from triangulum.controllers.base import BaseController
from triangulum.utils.enums import BrightSocietyTarget, DarkSocietyTarget, BrightSocietyAdmissionCondition, \
    DarkSocietyAdmissionCondition, SocietySharedInformation, SocietyAttitude


class Society(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='society')

    def get_shared_informations(self, village_id: int) -> dict:
        return self.invoke_action(
            action='getSharedInformations',
            params={
                'villageId': village_id,
            }
        )

    def create(
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

        return self.invoke_action(
            action='create',
            params=params
        )

    def invite(self, group_id: int, player_names: List[str], custom_text: str) -> dict:
        return self.invoke_action(
            action='invite',
            params={
                'groupId': group_id,
                'groupType': 2,  # Doesn't seem like there's any others right now
                'playerName': player_names,
                'customText': custom_text,
            }
        )

    def decline_invitation(self, id: int) -> dict:
        return self.invoke_action(
            action='declineInvitation',
            params={
                'id': id,
            }
        )

    def change_description(self, group_id: int, description: int) -> dict:
        return self.invoke_action(
            action='changeDescription',
            params={
                'groupId': group_id,
                'description': description,
            }
        )

    def close(self, group_id: int) -> dict:
        return self.invoke_action(
            action='close',
            params={
                'groupId': group_id,
                'groupType': 2,  # Doesn't seem like there's any others right now
            }
        )
