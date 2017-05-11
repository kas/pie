def is_cyclic(head):
    curr = head
    curr_lagging = head
    started = False

    if not curr:
        return False
    else:
        curr = curr.next

        while True:
            if curr is None:
                return False

            # if the fast pointer moves onto or over the slow pointer
            if curr == curr_lagging or ((curr == curr_lagging.next) and started):
                return True

            curr_lagging = curr_lagging.next
            curr = curr.next

            if curr is not None:
                curr = curr.next
            else:
                return False

            if not started:
                started = True
