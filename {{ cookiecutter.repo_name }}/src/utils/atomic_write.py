from atomicwrites import atomic_write as _backend_writer, AtomicWriter
from contextlib import contextmanager
import contextlib
import os
import io
import tempfile 

class SuffixWriter(AtomicWriter):
    """ SuffixWriter class that inherits from AtomicWriter """

    def get_fileobject(self, suffix="", prefix=tempfile.template, dir=None,
                       **kwargs):
        '''Return the temporary file to use.'''
        # raise error if target exists already
        if os.path.exists(self._path):
            raise FileExistsError()

        extension = self._path.split('.')[-1]
            
        if dir is None:
            dir = os.path.normpath(os.path.dirname(self._path))
        descriptor, name = tempfile.mkstemp(suffix='.'+extension, prefix=prefix,
                                            dir=dir)
        
        # io.open() will take either the descriptor or the name, but we need
        # the name later for commit()/replace_atomic() and couldn't find a way
        # to get the filename from the descriptor.

        os.close(descriptor)
        kwargs['mode'] = self._mode
        kwargs['file'] = name

        return io.open(**kwargs)


@contextmanager
def atomic_write(file, mode='w', as_file=True, new_default='asdf', **kwargs):
    """ Override the atomic_write function from atomicwrites """

    with _backend_writer(file, mode=mode, writer_cls=SuffixWriter, **kwargs) as f:
        # Return file object if as_file, otherwise return file path
        if as_file:
            yield f
        else:
            yield f.name