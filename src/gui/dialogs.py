# Copyright (C) 2016-2017 Frechdachs <frechdachs@rekt.cc>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


from os import path
from typing import List

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QInputDialog

from src import settings
from src.gui import SUPPORTED_SUB_FILES

_translate = QtCore.QCoreApplication.translate
_flags = (Qt.Dialog | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)

_FILTER_SUBS = " ".join(["*" + x for x in SUPPORTED_SUB_FILES])


def generate_file_name_proposal(video_file):
    nick = ("_" + settings.Setting_Custom_General_NICKNAME.value) or ""
    video = path.splitext(path.basename(video_file))[0] if video_file else _translate("Dialogs", "untitled")
    return "[QC]_{0}{1}.txt".format(video, nick)


def get_open_video(parent=None) -> path or None:
    """
    Will open a dialog to select a video to open.

    :param parent: The parent window
    :return: the selected file or None if abort
    """

    file_filter = _translate("Dialogs", "Video files") + " (*.mp4 *.mkv *.avi);;" + \
                  _translate("Dialogs", "All files") + " (*.*)"

    directory = settings.Setting_Internal_PLAYER_LAST_VIDEO_DIR.value

    return QFileDialog.getOpenFileName(
        parent=parent,
        caption=_translate("Dialogs", "Open Video File"),
        directory=directory,
        filter=file_filter
    )[0]


def get_open_subs(parent=None) -> List[str] or None:
    """
    Will open a dialog to select subtitles to open.

    :param directory: The directory to open initially
    :param parent: The parent window
    :return: the selected file or None if abort
    """

    file_filter = _translate("Dialogs", "Subtitle files") + " ({});;".format(_FILTER_SUBS) + \
                  _translate("Dialogs", "All files") + " (*.*)"

    directory = settings.Setting_Internal_PLAYER_LAST_SUB_DIR.value

    return QFileDialog.getOpenFileNames(
        parent=parent,
        caption=_translate("Dialogs", "Open Subtitle File"),
        directory=directory,
        filter=file_filter
    )[0]


def get_open_file_names(parent=None) -> List[str] or None:
    """
    Will open a dialog to select multiple qc documents.

    :param directory: The directory to open initially
    :param parent: The parent window
    :return: The selected files or None if abort
    """

    directory = settings.Setting_Internal_PLAYER_LAST_DOCUMENT_DIR.value

    return QFileDialog.getOpenFileNames(
        parent,
        _translate("Dialogs", "Open QC Document"),
        directory,
        _translate("Dialogs", "QC documents (*.txt);;All files (*.*)"),
    )[0]


def get_save_file_name(video_file: str, parent=None) -> path or None:
    """
    Will display a **Save as** dialog to the user.

    :param qc_doc: Current qc document path (full)
    :param video_file: The video file to save
    :param nick: The nickname to append
    :param parent: The parent window
    :return: the path to save or None if no video file was given
    """

    txt_proposal = generate_file_name_proposal(video_file)

    return QFileDialog.getSaveFileName(
        parent,
        _translate("Dialogs", "Save QC document as"),
        txt_proposal,
        _translate("Dialogs", "QC documents (*.txt);;All files (*.*)"),
    )[0]


def get_open_network_stream(parent) -> path or None:
    """
    Will display a dialog with a single QLineEdit input field.

    :param parent: The parent widget of this dialog
    :return: The URL or None if nothing was given
    """

    return QInputDialog.getText(
        parent,
        _translate("Dialogs", "Open network stream"),
        _translate("Dialogs", "Enter URL"),
        flags=Qt.WindowFlags(_flags),
    )[0]
