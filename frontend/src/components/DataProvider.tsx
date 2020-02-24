import * as React from 'react'
import {any} from "prop-types";

type DataProviderProps = {
    endpoint: string,
    render: Function
}


export class DataProvider extends React.Component<DataProviderProps> {
    state = {
        data: any,
        loaded: false,
        placeholder: "Loading... "
    };

    constructor(props: DataProviderProps) {
        super(props);

    };

    componentDidMount = async () => {
        console.log('compDidMount');
        try {
            const response = await fetch(this.props.endpoint);
            console.log(response);
            if (!response.ok) {
                console.log(response.statusText);
                return this.setState({placeholder: response.statusText});
            } else {
                const json = await response.json();
                console.log(json);
                this.setState({data: json, loaded: true});
            }
        } catch (error) {
            console.log(error);
        }
    };

    render() {
        const {data, loaded, placeholder} = this.state;
        return loaded ? this.props.render(data) : <p>{placeholder}</p>;
    };
}

