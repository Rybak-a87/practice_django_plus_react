import React, { useEffect, useState } from "react";
import axios from "axios";


function CategoryDetail({ match }) {
    const [category, setCategory] = useState({})
    const id = match.params.id

    useEffect(() => {
        axios({
            method: "GET",
            url: `http://127.0.0.1:8000/api/category/${id}`
        }).then(responce => {
            setCategory(responce.data)
        })
    }, [id])
    return (
        <div>
            Category with id {category.id}
            <p>Category: <strong>{category.name}</strong></p>
        </div>
    )
}

export default CategoryDetail;