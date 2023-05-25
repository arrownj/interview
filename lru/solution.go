package lru

import (
	"container/list"
)

type Cache struct {
	MaxEntries int
	Keys       *list.List
	Entries    map[string]*list.Element
}

type Item struct {
	Key   string
	Value interface{}
}

func NewLRU(maxEntries int) *Cache {
	keys := list.New()
	return &Cache{
		MaxEntries: maxEntries,
		Keys:       keys,
	}
}

func (c *Cache) Get(key string) (value interface{}, ok bool) {
	if element, ok := c.Entries[key]; ok {
		value := element.Value.(*Item).Value
		c.Keys.MoveToFront(element)
		return value, ok
	}
	return nil, false
}

func (c *Cache) Set(key string, value interface{}) {
	if element, ok := c.Entries[key]; ok {
		element.Value.(*Item).Value = value
		return c.Get(key)
	}
	if c.Keys.Len() >= c.MaxEntries {
		lastElement := c.Keys.Back()
		lastKey := lastElement.Value.(*Item).Key
		delete(c.Entries, key)
		c.Keys.Remove(lastElement)
	}
	element := &list.Element{
		list: c.Keys,
		Value: &Item{
			Key:   key,
			Value: value,
		},
	}
	c.Entries[key] = element
	c.Keys.PushFront(element)
}
