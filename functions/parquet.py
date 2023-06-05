def write_parquet(df, outpath):
    import sys
    import pyarrow as pa
    import pyarrow.parquet as pq
    table = pa.Table.from_pandas(df, preserve_index=False)
    pq.write_table(table, outpath)

def read_parquet(inpath):
    import sys
    import pyarrow as pa
    import pyarrow.parquet as pq
    return pq.read_table(inpath).to_pandas()