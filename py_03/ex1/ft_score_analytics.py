import sys


def main() -> None:
    valid_scores = []
    for element in sys.argv[1:]:
        try:
            valid_scores += [int(element)]
        except Exception:
            print(f"Invalid parameter : '{element}'")
    if len(valid_scores) == 0:
        print(
            "No scores provided. "
            "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
        )
        return
    print(f"Scores processed: {valid_scores}")
    print(f"Total players: {len(valid_scores)}")
    print(f"Total score: {sum(valid_scores)}")
    print(f"Average score: {(sum(valid_scores) / len(valid_scores)):.1f}")
    print(f"High score: {max(valid_scores)}")
    print(f"Low score: {min(valid_scores)}")
    print(f"Score range: {max(valid_scores) - min(valid_scores)}")


if __name__ == "__main__":
    print("=== Player score Analytics ===")
    main()
