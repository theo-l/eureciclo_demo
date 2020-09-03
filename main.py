import itertools


def solution(target, options: list):

    return sorted(
            [
                (sum(o) - target, o) for i in range(1, len(options) + 1)
                    for o in itertools.combinations(options, i) if sum(o) >= target
            ],
            key=lambda o: o[0] and len(o[1])
          )[0]


if __name__ == "__main__":
    result1 = solution(7, [1, 3, 4.5, 1.5, 3.5])
    assert result1[0] == 0.0
    assert set(result1[1]) == {1, 4.5, 1.5}

    # nesse caso, temos 2 opções para escolhe, [1, 6] ou [1, 4.5, 1.5], mas o resultado vai ser o tamnho melhor
    result2 = solution(7, [1, 6, 3, 4.5, 1.5, 3.5])
    assert result2[0] == 0.0
    assert set(result2[1]) == {1, 6}

    result3 = solution(5, [1, 3, 4.5, 1.5])
    assert result3[0] == 0.5
    assert set(result3[1]) == {1, 4.5}

    result4 = solution(4.9, [4.5, 0.4])
    assert result4[0] == 0.0
    assert set(result4[1]) == {4.5, 0.4}

