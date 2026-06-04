class Solution {
    public boolean isValid(String s) {
        // What we can do is have a hashmap, that keeps the brackets as keys, that givees us the O(1) lookup we need
        // We can iterate over the string, and add the opening brackets to a stack and if the order is correct, when we
        // Check the stack to compare it the closing bracket By pulling the bracket thats in the hashmap which is tied to
        // an opening bracket. That will let us know 1) if the order is correct, because we can check if the stack exists
        // IE that lets us know if we have a closing bracket but no pening bracket left then we've violated the rule
        // The second thing the next check will tell us is if it is the correct closing bracket IE it exists or not
        // third, if we're done iterating over the string but still have something in the tack, that means there 
        // were not enough closng brackets so we can return false. This ensures all the metrics are hit.
        // For the stack we can use Deque as it provides O(1) removal.

        Map<Character, Character> keys = new HashMap<>();
        Deque<Character> stack = new ArrayDeque();

        keys.put('}', '{');
        keys.put(')', '(');
        keys.put(']','[');

        for (char ch : s.toCharArray()) {
            if (keys.containsKey(ch)) {
                if (!stack.isEmpty() && stack.peek().equals(keys.get(ch))) {
                    // pop from the stack as it is a valid opening to closing
                    stack.pop();
                } else {
                    return false;
                }
            } else {
                stack.push(ch);
            }
        }

        return stack.isEmpty();
    }
}
