import React from 'react';
import Button from '@material-ui/core/Button';

const style = {
    margin: '10px',
    fontSize: '40px',
    fontWeight: '800',
    cursor: 'pointer',
    color: 'white',
    backgroundColor: 'black',
    outline: 'none'
};
const Square = ({ value , onClick }) => (
    <Button style={style} variant="outlined" onClick={onClick}>
        {value}
    </Button>
);

export default Square;