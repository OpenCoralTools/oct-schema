// Generated from LinkML schema: oct-schema




/// A coral entity.
class Coral {

    /// The name of the coral, e.g. "APAL001"
    String name;

    /// The number of coral specimens.
    int quantity;


    Coral({

        required this.name,

        required this.quantity

    });

    factory Coral.fromJson(Map<String, dynamic> json) => Coral(

        name: json["name"],

        quantity: json["quantity"]

    );

    Map<String, dynamic> toJson() => {

        "name": name,

        "quantity": quantity

    };
}



