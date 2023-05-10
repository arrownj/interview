package q1_stack_queue

import (
	"github.com/golang-collections/collections/stack"
)

type StackQueue struct {
	s1 *stack.Stack
	s2 *stack.Stack
}

func (sq *StackQueue) Push(value interface{}) {
	sq.s1.Push(value)
}

func (sq *StackQueue) Pop() interface{} {
	if sq.s2.Len() == 0 {
		for sq.s1.Len() > 0 {
			value := sq.s1.Pop()
			sq.s2.Push(value)
		}
	}
	if sq.s2.Len() == 0 {
		return nil
	}
	return sq.s2.Pop()
}

func (sq *StackQueue) Len() int {
	return sq.s1.Len() + sq.s2.Len()
}

func New() *StackQueue {
	return &StackQueue{
		s1: stack.New(),
		s2: stack.New(),
	}
}
