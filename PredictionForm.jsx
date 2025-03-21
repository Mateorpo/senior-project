import React, { useState, useEffect } from 'react';
import './PredictionForm.css';

const PredictionForm = ({ onPredict, isLoading }) => {
    const [inputs, setInputs] = useState({
        GrLivArea: 1000,         // Living area square feet
        LotArea: 5000,           // Lot size
        OverallQual: 7,          // Overall material quality (1-10)
        OverallCond: 5,          // Overall condition (1-10)
        YearBuilt: 1995,         // Year the house was built
        TotalBsmtSF: 1500        // Total basement area
    });

    const [isButtonEnabled, setIsButtonEnabled] = useState(false);

    useEffect(() => {
        if (isLoading) {
            setIsButtonEnabled(false);
            setTimeout(() => {
                setIsButtonEnabled(true);
            }, 3000);
        } else {
            setIsButtonEnabled(true);
        }
    }, [isLoading]);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setInputs(prevInputs => ({
            ...prevInputs,
            [name]: parseInt(value, 10) // Ensures the API gets numbers, not strings
        }));
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        onPredict(inputs);
    };

    return (
        <form className="prediction-form" onSubmit={handleSubmit}>
            <div className="form-group">
                <label htmlFor="GrLivArea">Living Area (sq ft):</label>
                <input
                    type="number"
                    id="GrLivArea"
                    name="GrLivArea"
                    value={inputs.GrLivArea}
                    onChange={handleChange}
                    min="500"
                    max="10000"
                    required
                />
            </div>
            <div className="form-group">
                <label htmlFor="LotArea">Lot Area (sq ft):</label>
                <input
                    type="number"
                    id="LotArea"
                    name="LotArea"
                    value={inputs.LotArea}
                    onChange={handleChange}
                    min="1000"
                    max="50000"
                    required
                />
            </div>
            <div className="form-group">
                <label htmlFor="OverallQual">Overall Quality (1-10):</label>
                <input
                    type="number"
                    id="OverallQual"
                    name="OverallQual"
                    value={inputs.OverallQual}
                    onChange={handleChange}
                    min="1"
                    max="10"
                    required
                />
            </div>
            <div className="form-group">
                <label htmlFor="OverallCond">Overall Condition (1-10):</label>
                <input
                    type="number"
                    id="OverallCond"
                    name="OverallCond"
                    value={inputs.OverallCond}
                    onChange={handleChange}
                    min="1"
                    max="10"
                    required
                />
            </div>
            <div className="form-group">
                <label htmlFor="YearBuilt">Year Built:</label>
                <input
                    type="number"
                    id="YearBuilt"
                    name="YearBuilt"
                    value={inputs.YearBuilt}
                    onChange={handleChange}
                    min="1800"
                    max="2024"
                    required
                />
            </div>
            <div className="form-group">
                <label htmlFor="TotalBsmtSF">Total Basement Area (sq ft):</label>
                <input
                    type="number"
                    id="TotalBsmtSF"
                    name="TotalBsmtSF"
                    value={inputs.TotalBsmtSF}
                    onChange={handleChange}
                    min="0"
                    max="5000"
                    required
                />
            </div>
            <button type="submit" className='submit-button' disabled={isLoading || !isButtonEnabled}>
                {isLoading ? 'Predicting...' : 'Predict Price'}
            </button>
        </form>
    );
};

export default PredictionForm;
