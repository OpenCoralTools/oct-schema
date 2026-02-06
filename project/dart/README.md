# Dart Classes

Dart class definitions for use in Flutter and Dart applications.

## Installation

Copy `lib/oct_schema.dart` into your project's `lib/` directory.

## Usage

```dart
import 'oct_schema.dart';

final coral = Coral(name: 'APAL001');

// JSON serialization
final json = coral.toJson();
final restored = Coral.fromJson(json);
```

## Features

- Full type safety for all schema classes
- camelCase property names
- Built-in `toJson()` and `fromJson()` methods
- Works with Flutter and pure Dart projects
