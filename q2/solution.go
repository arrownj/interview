package q2

/*
数组中出现次数前k多的数，比如[0,0,0,1,1,2],要求出现次数前2多的，输出0和1；出现次数前1多的，输出0
*/

type Item struct {
	Count int
	Value int
}

func (i Item) Compare(a, b *Item) int {
	return a.Count - b.Count
}

func Solution(nums []int, k int) []int {
	//maxSlice := MaxSlice(k, Item) //最大堆，容量为k的堆，当push一个元素时，容量未达到k则入堆并调整顺序，如果达到k，则将最小元素出堆，压入新元素调整顺序
	countMap := make(map[int]int)
	for _, num := range nums {
		if ok, count := countMap[num]; ok {
			countMap[num] = count + 1
		} else {
			countMap[num] = 1
		}
	}
	/*
		for key, value := countMap {
			maxSlice.Push(Item{Count: key, Value: value})
		}
		values := make([]int, k, k)
		for _, item := maxSlice.Items() {
			values = append(values, item.Key)
		}
	*/
	return values
}
