def flatten_list(head, tail):
  curr = head

  while curr:
    if curr.child:
      tail.append(curr.child)

    curr = curr.next
