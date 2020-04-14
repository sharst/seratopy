# seratopy
Easy access to serato crates in python


## Usage:

```
In [1]: from seratopy import Crate

In [2]: cr = Crate('/media/sharst/New Volume/_Serato_/Subcrates/Sloooow Techno.crate')

In [3]: print(cr)
Crate containing 81 tracks: 
DOWNLOAD Hard Techno/Adam Beyer - Space Date (Pleasurekraft Remix).mp3
DOWNLOAD Hard Techno/Adam Beyer - Your Mind (Will Clarke Remix).mp3
DOWNLOAD Hard Techno/Adam Beyer - Your Mind.mp3
DOWNLOAD Hard Techno/Alberto Ruiz - Expressor (Hell Driver Remix).mp3
...


In [4]: cr.track_path()
Out[4]: '/media/sharst/New Volume'

In [5]: cr.print_data()
[   ('vrsn', '1.0/Serato ScratchLive Crate'),
    ('osrt', [('brev', b'\x00')]),
    ('ovct', [('tvcn', 'key'), ('tvcw', '0')]),
    ('ovct', [('tvcn', 'artist'), ('tvcw', '0')]),
    ('ovct', [('tvcn', 'song'), ('tvcw', '0')]),
    ('ovct', [('tvcn', 'bpm'), ('tvcw', '0')]),
    ('ovct', [('tvcn', 'playCount'), ('tvcw', '0')]),
    ('ovct', [('tvcn', 'length'), ('tvcw', '0')]),
    ('ovct', [('tvcn', 'added'), ('tvcw', '0')]),
    (   'otrk',
        [   (   'ptrk',
                'DOWNLOAD Hard Techno/Adam Beyer - Space Date (Pleasurekraft '
                'Remix).mp3')]),
    (   'otrk',
        [   (   'ptrk',
                'DOWNLOAD Hard Techno/Adam Beyer - Your Mind (Will Clarke '
                'Remix).mp3')]),
    ('otrk', [('ptrk', 'DOWNLOAD Hard Techno/Adam Beyer - Your Mind.mp3')]),
...

In [6]: cr.add_track('/media/sharst/New Volume/T78 - Acid Lick.mp3')
Out[6]: True

In [7]: cr.save_to_file('/media/sharst/New Volume/New Crate.crate')


```
