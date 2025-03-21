import React from 'react';
import './PredictionResult.css';

const PredictionResult = ({ price, isLoading }) => {
    return (
        <div className="prediction-result">
            <h2>Predicted Price</h2>
            {isLoading ? (
                <p>Calculating...</p>
            ) : price !== null ? (
                <p className="price">${price.toLocaleString()}</p>
            ) : (
                <p>Fill up the fields to see the expected property price</p>
            )}
        </div>
    );
};

export default PredictionResult;
