from heap import Heap

def lfu_sim(cache_slots):
  cache_hit = 0
  tot_cnt = 0

  with open("C:\\Users\\gsmin2020\\Desktop\\SoongSilUniv\\2-1\\Data_structure\\lfu_sim\\linkbench.trc", 'r') as data_file:
    cache = Heap()
    for line in data_file.readlines():
      lpn = line.split()[0]
      tot_cnt += 1
      if cache.isCached(lpn):
        cache.cacheHit(lpn)
        cache_hit += 1
      else:
        if not cache.cacheInsert(lpn, cache_slots):
          cache.lfuDel()
          cache.cacheInsert(lpn, cache_slots)
    print(f"cache_slot = {cache_slots} | cache_hit = {cache_hit} | hit ratio = {cache_hit / tot_cnt}")

if __name__ == "__main__":
  for cache_slots in range(100, 1000, 100):
    lfu_sim(cache_slots)
