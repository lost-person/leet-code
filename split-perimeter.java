import java.lang.Math;
import java.util.Scanner;

class Point{
    double x;
    double y;

    /**
    * 计算两点间的距离
    * @param p1 点p1
    * @param p2 点p2
    * @return 距离
    */
    public static double getDist(Point p1, Point p2){
        return Math.sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y));
    }

    /**
    * 获取等分点
    * @param p1 点p1
    * @param p2 点p2
    * @param dist p1与p2的距离
    * @param len 在p1与p2连线的长度
    * @return 等分点
    */
    public static Point getSplitPoint(Point p1, Point p2, double dist, double len){
        Point splitPoint = new Point();
        // 利用长度比例计算点的坐标
        splitPoint.x = len / dist * (p1.x - p2.x) + p2.x;
        splitPoint.y = len / dist * (p1.y - p2.y) + p2.y;
        return splitPoint;
    }

    /**
    * 获取所有等分点
    * @param points 多边形的点的左边
    * @param splitPoints 多边形的等分店的坐标
    * @param k k等分
    */
    public static Point[] splitPerimeter(Point[] points, Point[] splitPoints, int k){
        int i = 0, j = 0, n = points.length;

        double l = 0;
        double[] dist = new double[n];
        // 计算周长
        for(; i < n - 1; i++){
            dist[i] = getDist(points[i], points[i + 1]);
            l += dist[i];
        }
        dist[i] = getDist(points[i], points[0]);
        l += dist[i];

        // 平均距离
        double avg = l / k;
        double sum_tmp = dist[0], tmp = 0;
        for(i = 0, j = 0; i < k; i++){
            while(j < n){
                // 跨点
                if(avg > sum_tmp){
                    j++;
                    sum_tmp += dist[j];
                }
                // 找到对应的边
                else{
                    tmp = sum_tmp - avg;
                    // 最后一个点
                    if(j + 1 == n){
                        splitPoints[i] = getSplitPoint(points[j], points[0], dist[j], tmp);
                    }
                    else{
                        splitPoints[i] = getSplitPoint(points[j], points[j + 1], dist[j], tmp);
                    }
                    sum_tmp = tmp;
                    break;
                }
            }
        }
        return splitPoints;
    }

    public static void main(String[] args) {
        // n边形，k等分
        int n = 0, k = 0;

        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        k = sc.nextInt();

        // 输入坐标
        int i = 0;
        Point[] points = new Point[n];
        Point[] splitPoints = new Point[k];
        for(; i < n; i++){
            Point p = new Point();
            p.x = sc.nextDouble();
            p.y = sc.nextDouble();
            points[i] = p;
        }
        sc.close();

        // 等分
        splitPoints = splitPerimeter(points, splitPoints, k);
        
        // 输出
        for(i = 0; i < k; i++)
            System.out.println("split point: x = " + splitPoints[i].x + '\t' + "y = " + splitPoints[i].y);
    }
}