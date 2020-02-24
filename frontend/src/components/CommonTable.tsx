import * as React from "react";

type PlaceProps = {
    id: number,
    name: string,
    email: string,
    created_at: string,
    created_by: string,
    description: string
}[]

export const CommonTable: React.FC<PlaceProps> = (props) => {
    return <div className="column">
        <table className="table is-striped">
            <thead>
            <tr>
                <td>Name</td>
                <td>Created</td>
            </tr>
            </thead>
            <tbody>
            {props.map((el) => <tr key={el.id}>
                <td>{el.name}</td>
                <td>{el.created_at}</td>
            </tr>)}
            </tbody>
        </table>
    </div>
};
export default CommonTable;