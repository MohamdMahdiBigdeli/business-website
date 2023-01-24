import React from 'react';
import Feature from './FeatureItem'
// import FeaturesData from '../../data/Features/features'
import axios from 'axios';
import { base_URL } from "../../helpers/BaseURL"

function Features({classes}) {
    const base_url = base_URL() + "features-data/"
    const [FeaturesData, setFeaturesData] = React.useState([])
    React.useEffect(() => {
        axios.get(base_url).then((Response) => {
            setFeaturesData(Response.data)
        })
    })

    return (
        <div className={`feature-area-wrapper ${classes}`}>
            <div className="container">
                <div className="row mtn-sm-60 mtn-md-5">
                    {
                        FeaturesData.map(feature=>(
                            <Feature key={feature.id} title={feature.title} text={feature.text} img={feature.imgSrc} />
                        ))
                    }
                </div>
            </div>
        </div>
    );
}

export default Features;