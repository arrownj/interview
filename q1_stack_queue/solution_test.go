package q1_stack_queue

import "testing"

func TestStackQueue(t *testing.T) {
	sq := New()
	sq.Push(1)
	sq.Push(2)
	value := sq.Pop()
	if value != 1 {
		t.Errorf("got %d, want %d", value, 1)
	}
	value = sq.Pop()
	if value != 2 {
		t.Errorf("got %d, want %d", value, 2)
	}
	value = sq.Pop()
	if value != nil {
		t.Errorf("got %d, want nil", value)
	}
}
