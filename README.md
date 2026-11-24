# The Funniest Out-of-Office

[![make.fun](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)
[![rank](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/yudhisutawan77/makefun-funniest-ooo/rank.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)
[![reward](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/yudhisutawan77/makefun-funniest-ooo/reward.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)

A [make.fun](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf) entry for **The Funniest Out-of-Office** — one line of out-of-office auto-reply, the funniest we can make it, in 140 characters or fewer.

## The entry

> I'm away this week. My inbox is now in the care of Fern, my houseplant: no thumbs, no opinions, and still a faster replier than I am.

(133 characters, one line.)

## How it works

`main.py` writes that single line to `/output/entry.txt` (or to the file named by `$ENTRY_OUT` when set). Nothing else — no image, no link, no second line.

```sh
python3 main.py
ENTRY_OUT=/tmp/entry.txt python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
