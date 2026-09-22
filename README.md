# alu-scripting

Scripting projects for the ALU Software Engineering program.

## Regular Expressions

Directory: [`regular_expressions`](./regular_expressions)

A series of Ruby scripts, each accepting a single command-line argument and
matching it against a specific regular expression.

| File | Description |
| --- | --- |
| `0-simply_match_school.rb` | Matches the literal string `School` (all occurrences) |
| `1-repetition_token_0.rb` | Matches `hb` + zero or more `t` + `n` (`*` repetition token) |
| `5-beginning_and_end.rb` | Matches a string that starts with `h`, ends with `n`, with exactly one character in between |
| `6-phone_number.rb` | Matches a 10-digit phone number with no separators |
| `7-OMG_WHY_ARE_YOU_SHOUTING.rb` | Extracts and concatenates every capital letter in a string |
| `8-textme.rb` | Parses a TextMe SMS log line into `sender,receiver,flags` |

### Usage

```bash
./regular_expressions/0-simply_match_school.rb "Best School"
```
