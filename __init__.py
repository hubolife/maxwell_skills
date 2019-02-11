# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'eward'

LOGGER = getLogger(__name__)


class AltSearch(MycroftSkill):
    def __init__(self):
        super(AltSearchSkill, self).__init__(name="AltSearch")

    def initialize(self):
        search_intent = IntentBuilder("SearchIntent"). \
            require("SearchKeyword").build()
        self.register_intent(search_intent, self.handle_search_intent)

        link_status_intent = IntentBuilder("link_statusIntent"). \
            require("link_statusKeyword").build()
        self.register_intent(how_are_you_intent,
                             self.handle_link_status_intent)

 
    def handle_search_intent(self, message):
        self.speak_dialog("alt.search.acromyn")

    def handle_how_are_you_intent(self, message):
        self.speak_dialog("link.status")

     def stop(self):
        pass


def create_skill():
    return AltSearchldSkill()
