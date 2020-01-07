from collections import Callable

from cachetools import TTLCache

from triangulum.controllers.base import BaseController
from triangulum.utils.cache import cached, MAX_SIZE, TTL
from triangulum.utils.dataclasses import MapFilter, AttacksFilter
from triangulum.utils.enums import PlayerTribe, SettingsTimeType, NotificationType, SettingsPremiumConfirmation, \
    Language, SettingsTimeFormat, OnlineStatusFilter, PlayerProgressTriggerHelpPage, RequestAction, ReportPlayerReason
from triangulum.utils.exceptions import ActionNotImplementedError


class Player(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='player')

    @cached(TTLCache(MAX_SIZE, TTL))
    async def get_all(self, device_dimension_x: int = 1920, device_dimension_y: int = 1080) -> dict:
        """Get all information about a players state in the gameworld

        Args:
            device_dimension_x: UI PARAM X dimension of the device
            device_dimension_y: UI PARAM Y dimension of the device
        """
        return await self.invoke_action(
            action='getAll',
            params={
                'deviceDimension': f'{device_dimension_x}:{device_dimension_y}'
            }
        )

    async def get_referral_direction(self) -> dict:
        """[*]
        """
        return await self.invoke_action(
            action='getReferralDirection'
        )

    async def choose_tribe(self, tribe_id: PlayerTribe) -> dict:
        """Choose a tribe to play as during registration

        Args:
            tribe_id: Tribe identifier
        """
        return await self.invoke_action(
            action='chooseTribe',
            params={
                'tribeId': tribe_id.value,
            }
        )

    @cached(TTLCache(MAX_SIZE, TTL))
    async def check_king_registration_rule(self) -> dict:
        """Check whether the player qualifies to play as a king *
        """
        return await self.invoke_action(
            action='checkKingRegistrationRule'
        )

    @cached(TTLCache(MAX_SIZE, TTL))
    async def get_system_message(self) -> dict:
        """Get system messages
        """
        return await self.invoke_action(
            action='getSystemMessage'
        )

    @cached(TTLCache(MAX_SIZE, TTL))
    async def get_achievement_notifications(self) -> dict:
        """[-]Get notifications of new achievements
        """
        return await self.invoke_action(
            action='getAchievementNotifications'
        )

    async def change_time_type(self, time_type: SettingsTimeType) -> dict:
        """[-]Change time type used

        Args:
            time_type: Time type to use
        """
        return await self.invoke_action(
            action='changeTimeType',
            params={
                'timeType': time_type.value,
            }
        )

    async def ping(self, cnt: int, last_global_message_time: float, last_id: int) -> dict:
        """[*]

        Args:
            cnt: UNKNOWN *
            last_global_message_time: UNKNOWN *
            last_id: UNKNOWN *
        """
        return await self.invoke_action(
            action='ping',
            params={
                'cnt': cnt,
                'lastGlobalMessageTime': last_global_message_time,
                'lastId': last_id,
            }
        )

    async def delete_all_notifications(self) -> dict:
        """[-]Delete all notifications
        """
        return await self.invoke_action(
            action='deleteAllNotifications'
        )

    @cached(TTLCache(MAX_SIZE, TTL))
    async def get_open_chat_windows(self) -> dict:
        """[-]Get info on open chat windows
        """
        return await self.invoke_action(
            action='getOpenChatWindows'
        )

    async def delete_notification(self, notification_type: NotificationType) -> dict:
        """[-]Delete a single notification of a particular type

        Args:
            notification_type: Type of notification
        """
        return await self.invoke_action(
            action='deleteNotification',
            params={
                'type': notification_type.value,
            }
        )

    async def get_cardgame_result(self) -> dict:
        """Get results of a finished cardgame *
        """
        return await self.invoke_action(
            action='getCardgameResult'
        )

    async def get_midnight(self) -> dict:
        """[*-]
        """
        return await self.invoke_action(
            action='getMidnight'
        )

    # TODO: These ids are incorrect, add ui_ids doc
    async def select_cards(
            self,
            first: bool,
            second: bool,
            third: bool,
            fourth: bool,
            fifth: bool
    ) -> dict:
        """Select cards in a card game

        Args:
            first: Toggle to select first card
            second: Toggle to select second card
            third: Toggle to select third card
            fourth: Toggle to select fourth card
            fifth: Toggle to select fifth card
        """
        return await self.invoke_action(
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

    @cached(TTLCache(MAX_SIZE, TTL))
    async def get_invitation_ref_link(self) -> dict:
        """Get referral url
        """
        return await self.invoke_action(
            action='getInvitationRefLink'
        )

    @cached(TTLCache(MAX_SIZE, TTL))
    async def get_player_info(self, player_id: int) -> dict:
        """Get information about a player

        Args:
            player_id: ID of the player
        """
        return await self.invoke_action(
            action='getPlayerInfo',
            params={
                'playerId': player_id,
            }
        )

    async def set_open_chat_windows(self, windows: list) -> dict:
        """[-]Set open chat windows

        Args:
            windows: ID of the windows
        """
        return await self.invoke_action(
            action='setOpenChatWindows',
            params={
                'windows': windows,  # TODO: type of this looks like "1.5230.4177", could be enumerable
            }
        )

    async def change_settings(
            self,
            premium_confirmation: SettingsPremiumConfirmation,
            language: Language,
            online_status_filter: OnlineStatusFilter,
            extended_simulator: bool,
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
        """Change in-game settings

        Args:
            premium_confirmation: Which premium actions should raise a confirmation dialog
            language: Language
            online_status_filter: Who should see when you're online
            extended_simulator: Whether combat simulator is toggled to use detailed simulations
            music_volume: Music volume
            sound_volume: Sound volume
            ui_sound_volume: UI sound volume
            mute_all: Toggle all sound to be muted
            time_type: Time type to use
            time_zone_switcher: Toggle time zone switcher in the UI
            time_format: Time format to use
            attacks_filter: Filter which attacks you don't want to see on the UI *
            map_filter: Filter which identifiers on the map you don't wish to see *
            enable_tab_notifications: Toggle to enable tab notifications on the UI
            disable_animations: Toggle to reduce animations on the UI
            enable_help_notifications: Toggle to enable help notifications on the UI
            enable_welcome_screen: Toggle to enable the welcome screen on the UI
            notepads_visible: Toggle notepad visibility
            _time_zone: Timezone to use
            _time_zone_string: Timezone string to use
        """
        return await self.invoke_action(
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

    async def add_note(self, x: int, y: int) -> dict:
        """[-]Create a note on the ui at a particular location

        Args:
            x: X location of the note
            y: Y location of the note
        """
        return await self.invoke_action(
            action='addNote',
            params={
                'x': x,
                'y': y,
            }
        )

    async def change_note(
            self,
            note_id: int,
            position_x: int,
            position_y: int,
            size_x: int,
            size_y: int,
            text: str
    ) -> dict:
        """[-]Change note data on the UI

        Args:
            note_id: ID of the note
            position_x: New position X of the note
            position_y: New position Y of the note
            size_x: Width of the note
            size_y: Height of the note
            text: Text on the note
        """
        return await self.invoke_action(
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

    async def remove_note(self, id: int) -> dict:
        """[-]Permanently deletes a note

        Args:
            id: ID of the note
        """
        return await self.invoke_action(
            action='removeNote',
            params={
                'id': id,
            }
        )

    async def get_activity_streams(self) -> dict:
        """[*]
        """
        return await self.invoke_action(
            action='getActivityStreams'
        )

    @cached(TTLCache(MAX_SIZE, TTL))
    async def get_prestige_conditions(self) -> dict:
        """Get conditions for weekly prestige point acquisition
        """
        return await self.invoke_action(
            action='getPrestigeConditions'
        )

    @cached(TTLCache(MAX_SIZE, TTL))
    async def get_robber_villages_amount(self, kingdom_id: int) -> dict:
        """[*]

        Args:
            kingdom_id: ID of a kingdom
        """
        return await self.invoke_action(
            action='getRobberVillagesAmount',
            params={
                'kingdomId': kingdom_id,
            }
        )

    async def reset_activity_stream(self) -> dict:
        """[*]
        """
        return await self.invoke_action(
            action='resetActivityStream'
        )

    # TODO: help_type Enum might be the wrong one
    async def trigger_in_game_help_notice(self, help_type: PlayerProgressTriggerHelpPage) -> dict:
        """UNKNOWN *

        Args:
            help_type: Type of help notice to trigger *
        """
        return await self.invoke_action(
            action='triggerInGameHelpNotice',
            params={
                'helpType': help_type.value,
            }
        )

    async def change_vacation_state(self) -> dict:
        """[*]
        """
        return await self.invoke_action(
            action='changeVacationState'
        )

    # TODO: This is triggered during account deletion, a token is sent back in the response
    # Payload example:
    # requestAction = 1
    # url = "https://com2x3.kingdoms.com/#/page:village/villId:536887296/subtab:Bids/playerId:5230/profileTab:settings/window:profile/prosubtab:Avatar/overlayprofile:startDeletion"
    async def request_verification(self, request_action: RequestAction, url: str) -> dict:
        """[*-]

        Args:
            request_action: UNKNOWN *
            url: UNKNOWN *
        """
        raise ActionNotImplementedError

        # return await self.invoke_action(
        #     action='requestVerification',
        #     params={
        #         'requestAction': request_action.value,
        #         'url': url,
        #     }
        # )

    # TODO: This is the other part of request_verification, where we send the token
    # that we receive in response to request_verification
    async def verify_action(self, token: str) -> dict:
        """[*-]

        Args:
            token: UNKNOWN *
        """
        raise ActionNotImplementedError

        # return await self.invoke_action(
        #     action='verifyAction',
        #     params={
        #         'token': token,
        #     }
        # )

    async def abort_deletion(self) -> dict:
        """Abort account deletion
        """
        return await self.invoke_action(
            action='abortDeletion'
        )

    async def request_external_login(self, public_site_key: int) -> dict:
        """Give account access to an external tool using a public site key

        Args:
            public_site_key: Public site key provided by the external tool
        """
        return await self.invoke_action(
            action='requestExternalLogin',
            params={
                'publicSiteKey': public_site_key,
            }
        )

    async def update_player_profile_content(self) -> dict:
        """[*]
        """
        return await self.invoke_action(
            action='updatePlayerProfileContent'
        )

    async def edit_profile(self, description: str) -> dict:
        """Edit your player profile description

        Args:
            description: New description
        """
        return await self.invoke_action(
            action='editProfile',
            params={
                'description': description,
            }
        )

    async def get_invitations_list(self) -> dict:
        """[*]Get list of friend invitations
        """
        return await self.invoke_action(
            action='getInvitationsList'
        )

    async def send_invitation(self, friend_name: str, email: str, own_name: str, message: str) -> dict:
        """[*]

        Args:
            friend_name: UNKNOWN *
            email: UNKNOWN *
            own_name: UNKNOWN *
            message: UNKNOWN *
        """
        return await self.invoke_action(
            action='sendInvitation',
            params={
                'friendName': friend_name,
                'email': email,
                'ownName': own_name,
                'message': message,
            }
        )

    async def report_conversation(self, room_id: str) -> dict:
        """[-]Begin a report on a conversation

        Args:
            room_id: ID of the conversation room
        """
        return await self.invoke_action(
            action='reportConversation',
            params={
                'roomId': room_id,
            }
        )

    async def report_conversation_finalize(self, room_id: str, comment: str) -> dict:
        """[-]Finalize the report initiated by report_conversation

        Args:
            room_id: ID of the room
            comment: Comment to attach to the report
        """
        return await self.invoke_action(
            action='reportConversationFinalize',
            params={
                'roomId': room_id,
                'comment': comment
            }
        )

    @cached(TTLCache(MAX_SIZE, TTL))
    async def get_player_influence(self, village_id: int) -> dict:
        """[*]Get influence over a player and their village

        Args:
            village_id: ID of the players village
        """
        return await self.invoke_action(
            action='getPlayerInfluence',
            params={
                'villageId': village_id,
            }
        )

    async def invite_to_kingdom(self, village_id: int) -> dict:
        """Invite a player to a kingdom

        Args:
            village_id: ID of the village within area of influence of a player to invite
        """
        return await self.invoke_action(
            action='inviteToKingdom',
            params={
                'villageId': village_id,
            }
        )

    async def report_player(self, room_id: str, player_id: int, reason: ReportPlayerReason) -> dict:
        """[-]Report a player

        Args:
            room_id: UNKNOWN *
            player_id: UNKNOWN *
            reason: UNKNOWN *
        """
        raise ActionNotImplementedError

        # return await self.invoke_action(
        #     action='reportPlayer',
        #     params={
        #         'roomId': room_id,
        #         'playerId': player_id,
        #         'reason': reason.value,
        #     }
        # )
