import gc


def release_memory(df):

    del df

    gc.collect()