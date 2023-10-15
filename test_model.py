import unittest
import mlops_model   
class TestMLOpsModel(unittest.TestCase):
    def test_model_predictions(self):
        #   sample dataset for testing
        sample_data = [[5.1, 3.5, 1.4, 0.2],  # Sample data for Iris Setosa
                       [6.3, 3.3, 4.7, 1.6],  # Sample data for Iris Versicolor
                       [6.4, 2.7, 5.3, 1.9]]  # Sample data for Iris Virginica

        # Ensure the model can make predictions without errors
        for data_point in sample_data:
            with self.subTest(data_point=data_point):
                try:
                    # Calling the mlops_model's prediction function  
                    prediction = mlops_model.predict(data_point)
                except Exception as e:
                    self.fail(f"Prediction error for data {data_point}: {str(e)}")

if __name__ == '__main__':
    unittest.main()
