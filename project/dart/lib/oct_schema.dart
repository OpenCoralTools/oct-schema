// Generated from LinkML schema: oct-schema




/// A coral entity.
class Coral {

    /// The name of the coral, e.g. "APAL001"
    String? name;


    Coral({

        this.name

    });

    factory Coral.fromJson(Map<String, dynamic> json) => Coral(

        name: json["name"]

    );

    Map<String, dynamic> toJson() => {

        "name": name

    };
}



