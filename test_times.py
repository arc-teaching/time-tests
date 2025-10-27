from times import compute_overlap_time, time_range


def test_generic_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    expected = [
        ("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
        ("2010-01-12 10:38:00", "2010-01-12 10:45:00"),
    ]
    assert compute_overlap_time(large, short) == expected


def test_ranges_dont_overlap():
    first = time_range("2010-01-12 10:00:00", "2010-01-12 10:30:00")
    second = time_range("2010-01-12 11:00:00", "2010-01-12 11:30:00")
    expected = []

    assert compute_overlap_time(first, second) == expected


def test_ranges_touching():
    first = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    second = time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00")
    expected = [("2010-01-12 11:00:00", "2010-01-12 11:00:00")]

    assert compute_overlap_time(first, second) == expected


def test_ranges_multiple_intervals():
    first = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00", 4)
    second = time_range(
        "2010-01-12 10:00:00", "2010-01-12 12:00:00", 4, gap_between_intervals_s=60
    )
    expected = [
        ("2010-01-12 10:00:00", "2010-01-12 10:15:00"),
        ("2010-01-12 10:15:00", "2010-01-12 10:29:15"),
        ("2010-01-12 10:30:15", "2010-01-12 10:45:00"),
        ("2010-01-12 10:45:00", "2010-01-12 10:59:30"),
    ]

    assert compute_overlap_time(first, second) == expected
