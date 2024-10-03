struct Point {
    int x;
    int y;
};

int distance(struct Point p1, struct Point p2) {
    return (p2.x - p1.x) * (p2.x - p1.x) + (p2.y - p1.y) * (p2.y - p1.y);
}