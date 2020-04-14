#!/usr/bin/python
import os

from base_data import BASE_DATA
from decoding import decode
from util import split_path


class Crate(object):
    def __init__(self, fname):
        self.data = []

        self.crate_path = os.path.dirname(os.path.abspath(fname))
        self.name = os.path.basename(fname)

        if os.path.exists(fname):
            self.load_from_file(fname)
        else:
            self.data = BASE_DATA

    def __str__(self):
        tracks = self.tracks()
        st = "Crate containing {} tracks: \n".format(len(tracks))
        st += "\n".join(tracks)
        return st

    def tracks(self):
        return [dat[1][0][1] for dat in self.data if dat[0] == 'otrk']

    def track_path(self):
        # Omit the _Serato_ and Subcrates folders at the end
        return os.path.join(*split_path(self.crate_path)[:-2])

    def remove_track(self, track_name):
        # track_name needs to include the containing folder name.
        for i, dat in enumerate(self.data):
            if dat[0] == 'otrk' and dat[1][0][1] == track_name:
                self.data.pop(i)
                return True

        return False

    def print_data(self):
        from pprint import PrettyPrinter
        printer = PrettyPrinter(indent=4)
        printer.pprint(self.data)

    def add_track(self, track_name):
        # track name must include the containing folder name
        track_name = os.path.relpath(os.path.join(self.track_path(), track_name),
                                     self.track_path())

        if track_name in self.tracks():
            return False

        self.data.append(('otrk', [('ptrk', track_name)]))
        return True

    def include_tracks_from_folder(self, folder_path):
        """
        Make this crate include all and only the files in the given folder
        """
        folder_tracks = os.listdir(folder_path)
        folder_tracks = [os.path.join(os.path.split(folder_path)[1], trck)
                         for trck in folder_tracks]

        for track in self.tracks():
            if track not in folder_tracks:
                self.remove_track(track)

        for mfile in folder_tracks:
            self.add_track(mfile)

    def load_from_file(self, fname):
        with open(fname, 'rb') as mfile:
            self.data = decode(mfile.read())

    def save_to_file(self, fname=None):
        if fname is None:
            fname = os.path.join(self.crate_path, self.name)

        enc_data = decode(self.data, reverse=True)
        with open(fname, 'wb') as mfile:
            mfile.write(enc_data)


