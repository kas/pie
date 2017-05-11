def is_cyclic(head):
  curr = head
  curr_lagging = head

  if not curr_lagging:
    return False
  else:
    curr = head.next

    while True:
      if curr is None:
        return False
      # if the fast pointer moves onto or over the slow pointer
      if curr == curr_lagging:
        return True
        
      curr_lagging = curr_lagging.next
      curr = curr.next

      if curr is not None:
        curr = curr.next
      else:
        return False
