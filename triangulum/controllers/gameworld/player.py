from collections import Callable

from triangulum.controllers.base import BaseController
from triangulum.utils.dataclasses import MapFilter, AttacksFilter
from triangulum.utils.enums import PlayerTribe, SettingsTimeType, NotificationType, SettingsPremiumConfirmation, \
    Language, SettingsTimeFormat, OnlineStatusFilter, PlayerProgressTriggerHelpPage, RequestAction, ReportPlayerReason
from triangulum.utils.exceptions import ActionNotImplementedError


class Player(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='player')

    def get_all(self, device_dimension_x: int, device_dimension_y: int) -> dict:
        return self.invoke_action(
            action='getAll',
            params={
                'deviceDimension': f'{device_dimension_x}:{device_dimension_y}'
            }
        )

    def get_referral_direction(self) -> dict:
        return self.invoke_action(
            action='getReferralDirection'
        )

    def choose_tribe(self, tribe_id: PlayerTribe) -> dict:
        return self.invoke_action(
            action='chooseTribe',
            params={
                'tribeId': tribe_id.value,
            }
        )

    def check_king_registration_rule(self) -> dict:
        return self.invoke_action(
            action='checkKingRegistrationRule'
        )

    def get_system_message(self) -> dict:
        return self.invoke_action(
            action='getSystemMessage'
        )

    def get_achievement_notifications(self) -> dict:
        return self.invoke_action(
            action='getAchievementNotifications'
        )

    def change_time_type(self, time_type: SettingsTimeType) -> dict:
        return self.invoke_action(
            action='changeTimeType',
            params={
                'timeType': time_type.value,
            }
        )

    def ping(self, cnt: int, last_global_message_time: float, last_id: int) -> dict:
        return self.invoke_action(
            action='ping',
            params={
                'cnt': cnt,
                'lastGlobalMessageTime': last_global_message_time,
                'lastId': last_id,
            }
        )

    def delete_all_notifications(self) -> dict:
        return self.invoke_action(
            action='deleteAllNotifications'
        )

    def get_open_chat_windows(self) -> dict:
        return self.invoke_action(
            action='getOpenChatWindows'
        )

    def delete_notification(self, notification_type: NotificationType) -> dict:
        return self.invoke_action(
            action='deleteNotification',
            params={
                'type': notification_type.value,
            }
        )

    def get_cardgame_result(self) -> dict:
        return self.invoke_action(
            action='getCardgameResult'
        )

    def get_midnight(self) -> dict:
        return self.invoke_action(
            action='getMidnight'
        )

    def select_cards(
            self,
            first: bool,
            second: bool,
            third: bool,
            fourth: bool,
            fifth: bool
    ) -> dict:
        return self.invoke_action(
            action='selectCards',
            params={
                'selectedCards': {
                    '1': first,
                    '2': second,
                    '3': third,
                    '4': fourth,
                    '5': fifth
                }
            }
        )

    def get_invitation_ref_link(self) -> dict:
        return self.invoke_action(
            action='getInvitationRefLink'
        )

    def get_player_info(self, player_id: int) -> dict:
        return self.invoke_action(
            action='getPlayerInfo',
            params={
                'playerId': player_id,
            }
        )

    def set_open_chat_windows(self, windows: list) -> dict:
        return self.invoke_action(
            action='setOpenChatWindows',
            params={
                'windows': windows,  # TODO: type of this looks like "1.5230.4177", could be enumerable
            }
        )

    def change_settings(
            self,
            premium_confirmation: SettingsPremiumConfirmation,
            language: Language,
            online_status_filter: OnlineStatusFilter,
            extended_simulator: bool,  # Detailed combat simulator toggle
            music_volume: int,
            sound_volume: int,
            ui_sound_volume: int,
            mute_all: bool,
            time_type: SettingsTimeType,
            time_zone_switcher: int,  # int bool
            time_format: SettingsTimeFormat,
            attacks_filter: AttacksFilter,
            map_filter: MapFilter,
            enable_tab_notifications: bool,
            disable_animations: bool,
            enable_help_notifications: bool,
            enable_welcome_screen: bool,
            notepads_visible: bool,
            _time_zone: float = 0.00,  # TODO: T5 has weird timezone implementation
            _time_zone_string: str = '±0:00',  # TODO: T5 has weird timezone implementation
    ) -> dict:
        return self.invoke_action(
            action='changeSettings',
            params={
                'newSettings': {
                    "premiumConfirmation": premium_confirmation.value,
                    "lang": language.value,
                    "onlineStatusFilter": online_status_filter.value,
                    "extendedSimulator": extended_simulator,
                    "musicVolume": music_volume,
                    "soundVolume": sound_volume,
                    "uiSoundVolume": ui_sound_volume,
                    "muteAll": mute_all,
                    "timeType": time_type.value,
                    "timeZone": _time_zone,
                    "timeZoneString": _time_zone_string,
                    "timeZoneSwitcher": time_zone_switcher,
                    "timeFormat": time_format.value,
                    "attacksFilter": attacks_filter.sum(),
                    "mapFilter": map_filter.sum(),
                    "enableTabNotifications": enable_tab_notifications,
                    "disableAnimations": disable_animations,
                    "enableHelpNotifications": enable_help_notifications,
                    "enableWelcomeScreen": enable_welcome_screen,
                    "notpadsVisible": notepads_visible  # NOTE: Typo on T5, not us
                },
            }
        )

    def add_note(self, x: int, y: int) -> dict:
        return self.invoke_action(
            action='addNote',
            params={
                'x': x,
                'y': y,
            }
        )

    def change_note(
            self,
            note_id: int,
            position_x: int,
            position_y: int,
            size_x: int,
            size_y: int,
            text: str
    ) -> dict:
        return self.invoke_action(
            action='changeNote',
            params={
                'newSettings': {
                    "id": note_id,
                    "positionX": position_x,
                    "positionY": position_y,
                    "sizeX": size_x,
                    "sizeY": size_y,
                    "text": text
                },
            }
        )

    def remove_note(self, id: int) -> dict:
        return self.invoke_action(
            action='removeNote',
            params={
                'id': id,
            }
        )

    def get_activity_streams(self) -> dict:
        return self.invoke_action(
            action='getActivityStreams'
        )

    def get_prestige_conditions(self) -> dict:
        return self.invoke_action(
            action='getPrestigeConditions'
        )

    def get_robber_villages_amount(self, kingdom_id: int) -> dict:
        return self.invoke_action(
            action='getRobberVillagesAmount',
            params={
                'kingdomId': kingdom_id,
            }
        )

    def reset_activity_stream(self) -> dict:
        return self.invoke_action(
            action='resetActivityStream'
        )

    # TODO: help_type Enum might be the wrong one
    def trigger_in_game_help_notice(self, help_type: PlayerProgressTriggerHelpPage) -> dict:
        return self.invoke_action(
            action='triggerInGameHelpNotice',
            params={
                'helpType': help_type.value,
            }
        )

    def change_vacation_state(self) -> dict:
        return self.invoke_action(
            action='changeVacationState'
        )

    # TODO: This is triggered during account deletion, a token is sent back in the response
    # Payload example:
    # requestAction = 1
    # url = "https://com2x3.kingdoms.com/#/page:village/villId:536887296/subtab:Bids/playerId:5230/profileTab:settings/window:profile/prosubtab:Avatar/overlayprofile:startDeletion"
    def request_verification(self, request_action: RequestAction, url: str) -> dict:
        raise ActionNotImplementedError

        # return self.invoke_action(
        #     action='requestVerification',
        #     params={
        #         'requestAction': request_action.value,
        #         'url': url,
        #     }
        # )

    # TODO: This is the other part of request_verification, where we send the token
    # that we receive in response to request_verification
    def verify_action(self, token: str) -> dict:
        raise ActionNotImplementedError

        # return self.invoke_action(
        #     action='verifyAction',
        #     params={
        #         'token': token,
        #     }
        # )

    def abort_deletion(self) -> dict:
        return self.invoke_action(
            action='abortDeletion'
        )

    def request_external_login(self, public_site_key: int) -> dict:
        return self.invoke_action(
            action='requestExternalLogin',
            params={
                'publicSiteKey': public_site_key,
            }
        )

    def update_player_profile_content(self) -> dict:
        return self.invoke_action(
            action='updatePlayerProfileContent'
        )

    def edit_profile(self, description: str) -> dict:
        return self.invoke_action(
            action='editProfile',
            params={
                'description': description,
            }
        )

    def get_invitations_list(self) -> dict:
        return self.invoke_action(
            action='getInvitationsList'
        )

    def send_invitation(self, friend_name: str, email: str, own_name: str, message: str) -> dict:
        return self.invoke_action(
            action='sendInvitation',
            params={
                'friendName': friend_name,
                'email': email,
                'ownName': own_name,
                'message': message,
            }
        )

    def report_conversation(self, room_id: str) -> dict:
        return self.invoke_action(
            action='reportConversation',
            params={
                'roomId': room_id,
            }
        )

    def report_conversation_finalize(self, room_id: str, comment: str) -> dict:
        return self.invoke_action(
            action='reportConversationFinalize',
            params={
                'roomId': room_id,
                'comment': comment
            }
        )

    def get_player_influence(self, village_id: int) -> dict:
        return self.invoke_action(
            action='getPlayerInfluence',
            params={
                'villageId': village_id,
            }
        )

    def invite_to_kingdom(self, village_id: int) -> dict:
        return self.invoke_action(
            action='inviteToKingdom',
            params={
                'villageId': village_id,
            }
        )

    def report_player(self, room_id: str, player_id: int, reason: ReportPlayerReason) -> dict:
        raise ActionNotImplementedError

        # return self.invoke_action(
        #     action='reportPlayer',
        #     params={
        #         'roomId': room_id,
        #         'playerId': player_id,
        #         'reason': reason.value,
        #     }
        # )
