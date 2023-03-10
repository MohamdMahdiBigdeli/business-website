import React from 'react';
import SectionTitle from '../UI/SectionTitle'
import ServiceItem from  './ServiceItem'
// import ServicesData from '../../data/Services/services'
import serviceTopBg from '../../assets/img/service/service-bg.jpg'
import axios from 'axios';
import { base_URL } from "../../helpers/BaseURL"

function Services({classes}) {
    const base_url = base_URL() + "services-data/"
    const [ServicesData, setServicesData] = React.useState([])
    React.useEffect(() => {
        axios.get(base_url).then((Response) => {
            setServicesData(Response.data)
        })
    })

    return (
        <div className={`service-area-wrapper ${classes}`}>
            <div className="service-area-top" style={{backgroundImage: `url("${serviceTopBg}")`}}>
                <div className="container">
                    <div className="row">
                        <div className="col-lg-6 col-xl-5 m-auto text-center">
                            <SectionTitle variant="light" title="خدمات ما" heading="ما راه پیشرفت شما را هموار می کنیم" />
                        </div>
                    </div>
                </div>
            </div>

            <div className="service-content-area">
                <div className="container">
                    <div className="row mtn-30">
                        {
                            ServicesData.map(service=>(
                                <ServiceItem key={service.id} id={service.id} title={service.title} text={service.shortDesc} thumb={service.thumb}/>
                            ))
                        }
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Services;
