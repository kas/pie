def unflatten_list(head, tail):
  curr = head

  while curr:
    if curr.child:
      curr.child.prev.next = None
      curr.child.prev = None
      unflatten_list(curr.child)

    curr = curr.next
