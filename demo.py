from seratopy import Crato


if __name__ == '__main__':
    print('Loading a serato crate...')
    cr = Crate('/media/sharst/New Volume/_Serato_/Subcrates/Sloooow Techno.crate')

    print('I am the following crate:')
    print(cr)

    print('This is the path where my files are stored:')
    cr.track_path()

    print('This is my internal data struct:')
    cr.print_data()

    print('Saving to a different file name..')
    cr.save_to_file('/media/sharst/New Volume/_Serato_/Subcrates/Sloooow Techno mirror.crate')

    print('Including all the tracks from a different folder..')
    cr.include_tracks_from_folder('/media/sharst/New Volume/DOWNLOAD Hard Techno')

    print('Overwriting the original file...')
    cr.save_to_file()
