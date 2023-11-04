import unittest
import pandas as pd

EXPECTED_DURATION = {
    "blank": 3,
    "breath_in": 2.7,
    "breath_in_last": 2.7,
    "breath_out": 2.3,
    "breath_out_last": 2.3,
    "cog": 0.5,
    "hold": 13,
    "hold_end": 2,
    "hold_test": 13,
    "hold_test_end": 2,
    "mot": 5,
    "movie": 1200,
    "vis": 3,
}

EXPECTED_ONSET = {
    "breath_holding_task.log": 153.0,
    "control_task": 295.5,
    "resting_state.log": 0.0,
}

PRECEDE = {
    "breath_freely": "hold_end",
    "breath_out": "breath_in",
    "hold": "breath_out_last",
    "hold_end": "hold",
    "hold_test": "breath_out_last",
}

REPETITION = {"mot": 2, "cog": 7}


class TestEvents(unittest.TestCase):
    """
    Tests that should pass for any log corresponding to our design
    """

    def __init__(self, data, *args, **kwargs):
        from write_event_file import write_event_file_from_log
        
        super(TestEvents, self).__init__(*args, **kwargs)

        if isinstance(data, pd.DataFrame):
            self.events = data
        elif isinstance(data, str):
            self.events = write_event_file_from_log(data)
        else:
            raise ValueError("Input 'data' must be a DataFrame or a string.")

    def test_durations(self):
        for trial_type, expected_duration in EXPECTED_DURATION.items():
            if trial_type in self.events["trial-type"].values:
                indices = self.events[self.events["trial-type"] == trial_type].index
                for index in indices:
                    self.assertAlmostEqual(
                        self.events.loc[index, "duration"], expected_duration, places=1
                    )

    def test_onset(self):
        expected_onset = EXPECTED_ONSET[self.log]
        self.events
        for trial_type, expected_onset in EXPECTED_ONSET.items():
            if trial_type in self.log.keys:
                indices = self.events[self.events["trial-type"] == trial_type].index
                for index in indices:
                    self.assertAlmostEqual(
                        self.events.loc[index, "onset"], expected_onset, places=1
                    )

    def test_precede(self):
        for trial_type, preceding_type in PRECEDE.items():
            if trial_type in self.events["trial-type"].values:
                indices = self.events[self.events["trial-type"] == trial_type].index
                for index in indices:
                    prev_index = index - 1
                    if prev_index >= 0:
                        self.assertEqual(
                            self.events.loc[prev_index, "trial-type"], preceding_type
                        )

    def test_repetition(self):
        for trial_type, expected_repetitions in REPETITION.items():
            if trial_type in self.events["trial-type"].values:
                indices = self.events[self.events["trial-type"] == trial_type].index
                for i in range(len(indices) - 1):
                    self.assertEqual(indices[i + 1] - indices[i], expected_repetitions)

    def test_movie_onset(self):
        movie_onset = self.events[self.events["trial-type"] == "movie"]["onset"].values
        self.assertAlmostEqual(movie_onset, 0.0, places=1)


class TestEventsSpecific(unittest.TestCase):
    """
    Tests that should pass for the particular log saved for code testing
    """

    def __init__(self, data, *args, **kwargs):
        super(TestEvents, self).__init__(*args, **kwargs)
        self.events = write_event_file_from_log(data)

    def test_onset(self):
        expected_onset = EXPECTED_ONSET[self.log]
        self.events
        for trial_type, expected_onset in EXPECTED_ONSET.items():
            if trial_type in self.log.keys:
                indices = self.events[self.events["trial-type"] == trial_type].index
                for index in indices:
                    self.assertAlmostEqual(
                        self.events.loc[index, "onset"], expected_onset, places=1
                    )


if __name__ == "__main__":
    # Create a test suite
    suite = unittest.TestSuite()

    # Add test cases with different input data
    for log in ["resting_state.log", "control_task.log", "breath_holding_task.log"]:
        # Run the tests that should pass for any input
        test_case = TestEvents
        test_case.__name__ = "Test_{}".format(log)
        setattr(test_case, "log", log)
        suite.addTest(unittest.makeSuite(test_case))

        # Additionally run the tests that should pass for these particular logs
        test_case = TestEventsSpecific
        test_case.__name__ = "TestSpecific_{}".format(log)
        setattr(test_case, "log", log)
        suite.addTest(unittest.makeSuite(test_case))

    # Run the test suite
    unittest.TextTestRunner(verbosity=2).run(suite)
