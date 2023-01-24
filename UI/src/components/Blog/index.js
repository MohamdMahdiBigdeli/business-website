import React from 'react';
import SectionTitle from "../UI/SectionTitle";
import BlogItem from "./blogItem";
import Blogs from '../../data/Blog/blog';
import axios from 'axios';
import { base_URL } from "../../helpers/BaseURL"

function Blog() {
    const base_url = base_URL() + "blog-data/"
    const [Blogs, setBlogs] = React.useState([])
    React.useEffect(() => {
        axios.get(base_url).then((Response) => {
            setBlogs(Response.data)
        })
    })

    return (
        <div className="blog-area-wrapper sm-top">
            <div className="container">
                <div className="row">
                    <div className="col-12 text-center">
                        <SectionTitle title="وبلاگ ما" heading="آخرین به روزرسانی ها"/>
                    </div>
                </div>

                <div className="row mtn-35">
                    {
                        Blogs.reverse().slice(0,3).map(blog =>(
                            <BlogItem key={blog.id} id={blog.id} title={blog.title} excerpt={blog.excerpt} postBy={blog.author.name} date={blog.publishDate}/>
                        ))
                    }
                </div>
            </div>
        </div>
    );
}

export default Blog;
